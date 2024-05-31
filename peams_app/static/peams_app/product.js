const addItemBtn = document.getElementById('addItemBtn');
        const inventoryChartCanvas = document.getElementById('inventoryChart');
        const inventoryChartCtx = inventoryChartCanvas.getContext('2d');

        // Dummy data for inventory tracking
        const inventoryData = {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: 'Inventory Level',
                data: [100, 120, 90, 150, 130, 110, 140, 160, 180, 170, 190, 200],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        };
        //Dummy Inventory tracking chart
        const inventoryChart = new Chart(inventoryChart, {
            type: 'line',
            data: inventoryData,
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

        // Add event listener for "Add Item" button
        addItemBtn.addEventListener('click', function() {
            // Add item logic here
            console.log('Add Item button clicked');
        });