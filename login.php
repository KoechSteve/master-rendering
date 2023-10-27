<?php
<head>
    <title>Login</title>
</head>
<body>
    <?php
    // Check if the form has been submitted
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        // Retrieve user input
        $username = $_POST['username'];
        $password = $_POST['password'];

        // Replace this with your authentication logic (e.g., database query)
        // In a real application, you'd validate the user's credentials and set up sessions for logged-in users.
        // For this example, we're simply checking if the username and password are 'admin'.
        if ($username == 'admin' && $password == 'admin') {
            echo "Login successful! Welcome, $username.";
        } else {
            echo "Login failed. Please check your credentials.";
        }
    }
    ?>
    <h1>Login</h1>
    <form action="login.php" method="POST">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
?>
