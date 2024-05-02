const searchField = document.querySelector('#searchField');
const tableOutput = document.querySelector('.table-output');
const appTable = document.querySelector('.app-table');




tableOutput.style.display = 'none';

searchField.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;
    if (searchValue.trim().length > 0) {
        console.log('searchValue:', searchValue);
        fetch('/search_expenses', {
            body: JSON.stringify({ searchText: searchValue }),
            method: 'POST',
        })
            .then((res) => res.json())
            .then((data) => {
                console.log('data:', data);
                tableOutput.style.display = 'block';
                appTable.style.display = 'none';
                let output = '';
                if (data.length === 0) {
                    tableOutput.innerHTML = 'No results';
                    return;
                }  else {
                    data.forEach((expense) => {
                        output += `
                        <tr>
                            <td>${expense.amount}</td>
                            <td>${expense.description}</td>
                            <td>${expense.date}</td>
                            <td>${expense.category}</td>
                            <td>
                            <a href="{% url 'edit' expense.id %}" type="button" class="btn btn-outline-info">Edit</a>
                            <a href="{% url 'delete' expense.id %}" class="btn btn-outline-danger"><i class="bi bi-x-circle"></i></a>
                        </td>
                        </tr>
                        `;
                    });
                    document.querySelector('tbody').innerHTML = output;
                }
                
            });
    } 

});
