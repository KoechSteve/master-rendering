<?php
<head>
    <title>Admin Page</title>
</head>
<body>
    <h1>Admin Page</h1>
    <h2>Add Client</h2>
    <form action="admin.php" method="POST">
        <label for="client_name">Client Name:</label>
        <input type="text" name="client_name" required>
        <button type="submit" name="add_client">Add Client</button>
    </form>

    <h2>Add Renderer</h2>
    <form action="admin.php" method="POST">
        <label for="renderer_name">Renderer Name:</label>
        <input type="text" name="renderer_name" required>
        <label for="days_worked">Days Worked:</label>
        <input type="number" name="days_worked" required>
        <label for="pay_per_day">Pay Per Day:</label>
        <input type="number" name="pay_per_day" required>
        <button type="submit" name="add_renderer">Add Renderer</button>
    </form>

    <h2>Client List</h2>
    <ul>
        <?php
        // Display the list of clients
        $results = $db->query('SELECT * FROM clients');
        while ($row = $results->fetchArray()) {
            echo '<li>' . $row['name'] . ' <a href="admin.php?delete_client=' . $row['id'] . '">Delete</a></li>';
        }
        ?>
    </ul>

    <h2>Renderer List</h2>
    <ul>
        <?php
        // Display the list of renderers
        $results = $db->query('SELECT * FROM renderers');
        while ($row = $results->fetchArray()) {
            $total_pay = $row['days_worked'] * $row['pay_per_day'];
            echo '<li>' . $row['name'] . ' (Days Worked: ' . $row['days_worked'] . ', Pay per Day: $' . $row['pay_per_day'] . ', Total Pay: $' . $total_pay . ') <a href="admin.php?delete_renderer=' . $row['id'] . '">Delete</a></li>';
        }
        ?>
    </ul>

    <?php
    // Handle adding and deleting clients and renderers
    if (isset($_POST['add_client'])) {
        $client_name = $_POST['client_name'];
        $db->exec("INSERT INTO clients (name) VALUES ('$client_name')");
    }

    if (isset($_POST['add_renderer'])) {
        $renderer_name = $_POST['renderer_name'];
        $days_worked = (int)$_POST['days_worked'];
        $pay_per_day = (float)$_POST['pay_per_day'];
        $db->exec("INSERT INTO renderers (name, days_worked, pay_per_day) VALUES ('$renderer_name', $days_worked, $pay_per_day)");
    }

    if (isset($_GET['delete_client'])) {
        $client_id = (int)$_GET['delete_client'];
        $db->exec("DELETE FROM clients WHERE id = $client_id");
    }

    if (isset($_GET['delete_renderer'])) {
        $renderer_id = (int)$_GET['delete_renderer'];
        $db->exec("DELETE FROM renderers WHERE id = $renderer_id");
    }
    ?>
</body>
?>
