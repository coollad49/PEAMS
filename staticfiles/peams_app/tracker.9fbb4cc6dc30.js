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
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${entry.date}</td>
        <td>${entry.item}</td>
        <td>${entry.expiration}</td>
    `;
    calendarBody.appendChild(row);

});

// Get the modal and modal message elements
const modal = document.getElementById("myModal");
const modalMessage = document.getElementById("modalMessage");

// Get the <span> element that closes the modal
const span = document.getElementsByClassName("close")[0];

// When the user clicks on the close button, close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function searchCalendarEntries() {
    const searchInput = document.getElementById('searchInput');
    const searchTerm = searchInput.value.trim().toLowerCase();

    if (searchTerm) {
        const foundEntry = sampleEntries.find(entry => entry.item.toLowerCase().includes(searchTerm));

        if (foundEntry) {
            modalMessage.textContent = `Found entry: ${foundEntry.item} (Expiration: ${foundEntry.expiration})`;
            modal.style.display = "block";
        } else {
            modalMessage.textContent = "No matching entry found.";
            modal.style.display = "block";
        }
    }
}
// function getCurrentDate() {
//     const today = new Date();
//     return `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
// }

