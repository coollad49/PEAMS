// JavaScript code goes here
const expiringTodayCount = 5;
const expiredCount = 2;
const notificationsCount = 3;

// Update the dashboard summary
document.getElementById('expiring-soon').textContent = expiringTodayCount;
document.getElementById('expired').textContent = expiredCount;
document.getElementById('notifications').textContent = notificationsCount;

// Add sample calendar entries
const calendarBody = document.getElementById('calendar-body');
const sampleEntries = [
    { date: '2023-06-15', item: 'Milk', expiration: '2023-06-30' },
    { date: '2023-07-01', item: 'Eggs', expiration: '2023-07-15' },
    { date: '2023-08-01', item: 'Cheese', expiration: '2023-08-31' }
];

sampleEntries.forEach(entry => {
    addCalendarEntry(entry.date, entry.item, entry.expiration);
});

function addNewItem() {
    const newItemInput = document.getElementById('new-item-input');
    const newItem = newItemInput.value.trim();
    if (newItem) {
        const expirationDate = prompt('Enter the expiration date (YYYY-MM-DD):');
        addCalendarEntry(getCurrentDate(), newItem, expirationDate);
        newItemInput.value = '';
    }
}

function addCalendarEntry(date, item, expiration) {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${date}</td>
        <td>${item}</td>
        <td>${expiration}</td>
    `;
    calendarBody.appendChild(row);
}

function getCurrentDate() {
    const today = new Date();
    return `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
}
