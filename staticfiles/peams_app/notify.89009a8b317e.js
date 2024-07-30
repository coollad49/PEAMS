// Sample data for product expiry alerts
const alerts = [
    { id: 1, product: 'Product A', expiryDate: '2024-06-01', type: 'expired' },
    { id: 2, product: 'Product B', expiryDate: '2024-05-30', type: 'warning' },
    // Add more alerts as needed
];

// Function to render notification items
function renderNotification(alert) {
    const notificationList = document.querySelector('.notifications-list');
    const notification = document.createElement('li');
    notification.classList.add('notification', alert.type);
    notification.textContent = `${alert.product} expires on ${alert.expiryDate}`;
    notificationList.appendChild(notification);
}

// Render notifications
alerts.forEach(alert => renderNotification(alert));