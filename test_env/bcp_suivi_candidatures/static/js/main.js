console.log('Testing')
var expanded = false;
var candidatesList, filteredList = candidatesList;
const statusField = { 
    V: "Validé",
    A: "En attente",
}
console.log(Object.keys(statusField));

var string = "hello";


const getCandidates = async() => {
    try {
        const res = await fetch('/candidates/data')
        if (!res.ok) {
            throw new Error(`Response status: $(res.status)`);
        };
        const json = JSON.parse(await res.json());
        const data = Array.from(json);
        return data
    } catch (error) {
        console.error(error.message);
    };
}







function showCheckboxes() {
    var checkboxes = document.getElementById("checkboxes");
    if (!expanded) {
        checkboxes.style.display = "block";
        expanded = true;
    } else {
        checkboxes.style.display = "none";
        expanded = false;
    };
}

function details(id) {
    window.location.href = `/candidates/${id}`;
}

function loadItems(status) {
    select = document.getElementById("id_status");
    select.innerHTML = '';
    for (key in statusField)
    {
        if (status == key) {
            select.innerHTML += `<option value="${key}" selected>${statusField[key]}</option>`
        } else {
            select.innerHTML += `<option value="${key}">${statusField[key]}</option>`
        };
    };
};

function searchPosition() {
    query = document.getElementById("position_search").value;
    if (query != "") { 
        filteredList = filteredList.filter(element => element.fields.position.toLowerCase().includes(query.toLowerCase()));
    };


}

function filterStatus() {
    all_status = document.getElementById("status-all");
    if (!all_status.checked) {
        var count = 0;
        for (var i = 1; i <= 2; i++) {
            if (!document.getElementById(`status-${i}`).checked) {
                filteredList = filteredList.filter(element => element.fields.status != document.getElementById(`status-${i}`).value);
            } else {
                count++;
            };
        };
    } else {
        for (var i = 1; i <= 2; i++)
        {
            document.getElementById(`status-${i}`).checked = true;
        };
    };
}

async function filter() {
    candidatesList = await getCandidates()
    console.log(candidatesList);
    var table = document.getElementById("table-content");
    filteredList = candidatesList;
    searchPosition();
    filterStatus();
    table.innerHTML = '';
    filteredList.forEach(element => {
        candidate = element.fields;
        table.innerHTML += `
            <tr onclick="details(${element.pk})">
                <td>
                    ${candidate.name}
                </td>
                <td>
                    <a class="cv_link" href="../media/${candidate.cv}" target="_blank">Apercu</a>
                </td>
                <td>
                    ${statusField[candidate.status]}
                </td>
                <td>
                    ${candidate.position}
                </td>
        `;
    });
}

function fillCvLink() {
    link = document.querySelector(".download-button");
    link.href = document.getElementById("id_cv");
}