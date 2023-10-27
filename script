document.addEventListener('DOMContentLoaded', function() {
    // Simulated rendering queue data
    const queueData = [
        { id: 1, name: 'example.jpg', status: 'Pending' },
        // Add more queue items here
    ];

    const fileTable = document.getElementById('file-table');

    // Populate the rendering queue table
    queueData.forEach(item => {
        const row = fileTable.insertRow();
        row.innerHTML = `
            <td>${item.id}</td>
            <td>${item.name}</td>
            <td>${item.status}</td>
            <td><a href="/preview/${item.id}">View</a></td>
        `;
    });
});
