function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const searchedText = document.getElementById('searchField').value;
      const tableRowElements = document.querySelectorAll('tbody tr');

      for (const row of tableRowElements) {
         const cellData = row.querySelectorAll('td');
         let isSelected = false;

         row.classList.remove('select')

         for (const cell of cellData) {
            if (cell.textContent.toLowerCase().includes(searchedText.toLowerCase())) {
               isSelected = true;
               break;
            }
         }

         if (isSelected) {
            row.classList.add('select');
         }
      }

      searchedText.value = '';
   }
}