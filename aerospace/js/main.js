document.addEventListener('DOMContentLoaded', () => {
    const grid = document.getElementById('aircraft-grid');
    const manufacturerSelect = document.getElementById('manufacturer-select');
    const typeSelect = document.getElementById('type-select');
    const searchInput = document.getElementById('search-input');

    let aircraftData = [];

    // Fetch Data
    fetch('data/aircraft.json')
        .then(response => response.json())
        .then(data => {
            aircraftData = data;
            populateFilters();
            renderGrid(aircraftData);
        })
        .catch(error => {
            console.error('Error loading data:', error);
            grid.innerHTML = '<p class="error">Failed to load aircraft data.</p>';
        });

    // Render Grid
    function renderGrid(data) {
        grid.innerHTML = '';

        if (data.length === 0) {
            grid.innerHTML = '<p class="no-results">No aircraft found matching your criteria.</p>';
            return;
        }

        data.forEach(aircraft => {
            const card = document.createElement('a');
            card.href = `detail.html?id=${aircraft.id}`;
            card.className = 'card';
            
            card.innerHTML = `
                <img src="${aircraft.image}" alt="${aircraft.name}" class="card-image">
                <div class="card-content">
                    <div class="card-meta">
                        <span>${aircraft.manufacturer}</span>
                        <span>${aircraft.year_made}</span>
                    </div>
                    <h3 class="card-title">${aircraft.name}</h3>
                    <p class="card-info">${aircraft.type}</p>
                    <div class="card-footer">
                        <span>Operator: ${aircraft.operator}</span>
                        <span>Details &rarr;</span>
                    </div>
                </div>
            `;
            grid.appendChild(card);
        });
    }

    // Populate Filters
    function populateFilters() {
        const manufacturers = [...new Set(aircraftData.map(a => a.manufacturer))].sort();
        const types = [...new Set(aircraftData.map(a => a.type))].sort();

        manufacturers.forEach(m => {
            const option = document.createElement('option');
            option.value = m;
            option.textContent = m;
            manufacturerSelect.appendChild(option);
        });

        types.forEach(t => {
            const option = document.createElement('option');
            option.value = t;
            option.textContent = t;
            typeSelect.appendChild(option);
        });
    }

    // Filter Logic
    function filterData() {
        const manufacturer = manufacturerSelect.value;
        const type = typeSelect.value;
        const search = searchInput.value.toLowerCase();

        const filtered = aircraftData.filter(item => {
            const matchManufacturer = manufacturer === 'all' || item.manufacturer === manufacturer;
            const matchType = type === 'all' || item.type === type;
            const matchSearch = item.name.toLowerCase().includes(search) || 
                                item.manufacturer.toLowerCase().includes(search) ||
                                item.operator.toLowerCase().includes(search);

            return matchManufacturer && matchType && matchSearch;
        });

        renderGrid(filtered);
    }

    // Event Listeners
    manufacturerSelect.addEventListener('change', filterData);
    typeSelect.addEventListener('change', filterData);
    searchInput.addEventListener('input', filterData);
});
