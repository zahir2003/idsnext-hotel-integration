
const API_URL = "http://127.0.0.1:8000";
const output = document.getElementById("output");

async function requestAPI(path, method = "GET") {
    output.textContent = "Loading...";

    try {
        const response = await fetch(API_URL + path, { method });
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Request failed");
        }

        output.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        output.textContent = "Error: " + error.message;
    }
}

function loadData(resource) {
    requestAPI(`/api/${resource}`);
}

function syncReservations() {
    requestAPI("/api/sync/reservations", "POST");
}
