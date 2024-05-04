const searchField = document.querySelector('#searchField');
const tableOutput = document.querySelector('.table-output');
const appTable = document.querySelector('.app-table');
const paginationContainer = document.querySelector('.pagination-container');
const tableBody = document.querySelector('.table-body');
const noResults = document.querySelector('.no-results');


tableOutput.style.display = 'none';
noResults.style.display = 'none';
searchField.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;
    if (searchValue.trim().length > 0) {
        console.log('searchValue:', searchValue);
        paginationContainer.style.display = 'none';
        tableBody.innerHTML = '';
        fetch('search_incomes', {
            body: JSON.stringify({ searchText: searchValue }),
            method: 'POST',
        })
            .then((res) => res.json())
            .then((data) => {
                console.log('data:', data);
                tableOutput.style.display = 'block';
                appTable.style.display = 'none';
                
                if (data.length === 0) {
                    tableOutput.style.display = 'none';
                    noResults.style.display = 'block';
                } else {
                    noResults.style.display = 'none';
                    data.forEach((income) => {
                        tableBody.innerHTML+= `
                        <tr>
                            <td>${income.amount}</td>
                            <td>${income.description}</td>
                            <td>${income.date}</td>
                            <td>${income.source}</td>
                            <td>
                            <a href="{% url 'edit' income.id %}" type="button" class="btn btn-outline-info">Edit</a>
                            <a href="{% url 'delete' income.id %}" class="btn btn-outline-danger"><i class="bi bi-x-circle"></i></a>
                        </td>
                        </tr>
                        `;
                    });
                }
                
            });
    } else {
        noResults.style.display = 'none';
        tableOutput.style.display = 'none';
        appTable.style.display = 'block';
        paginationContainer.style.display = 'block';
    } 

});
