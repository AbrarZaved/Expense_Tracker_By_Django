const searchField = document.querySelector('#searchField');
const tableOutput = document.querySelector('.table-output');
const appTable = document.querySelector('.app-table');
const paginationContainer = document.querySelector('.pagination-container');





tableOutput.style.display = 'none';

searchField.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;
    if (searchValue.trim().length > 0) {
        console.log('searchValue:', searchValue);
        paginationContainer.style.display = 'none';
        fetch('/search_expenses', {
            body: JSON.stringify({ searchText: searchValue }),
            method: 'POST',
        })
            .then((res) => res.json())
            .then((data) => {
                console.log('data:', data);
                tableOutput.style.display = 'block';
                appTable.style.display = 'none';
                
                if (data.length === 0) {
                    tableOutput.innerHTML = 'No results';
                    
                    return;
                }  else {
                    appTable.style.display = 'block';
                    paginationContainer.style.display = 'block';
                    
                }
                
            });
    } 

});
