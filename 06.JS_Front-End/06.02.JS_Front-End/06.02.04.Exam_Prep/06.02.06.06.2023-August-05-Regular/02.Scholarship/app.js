window.addEventListener("load", solve);

function solve() {
    const studentInput = document.getElementById('student');
    const universityInput = document.getElementById('university');
    const scoreInput = document.getElementById('score');

    const previewList = document.getElementById('preview-list');
    const candidatesList = document.getElementById('candidates-list')

    const nextButton = document.getElementById('next-btn');
    nextButton.addEventListener('click', () => {
        const student = studentInput.value;
        const university = universityInput.value;
        const score = scoreInput.value;

        if (student !== '' && university !== '' && score !== '') {
            // editButton;
            const editButton = document.createElement('button');
            editButton.className = 'action-btn edit';
            editButton.textContent = 'edit';

            // applyButton;
            const applyButton = document.createElement('button');
            applyButton.className = 'action-btn apply';
            applyButton.textContent = 'apply';

            // h4Name;
            const h4Name = document.createElement('h4');
            h4Name.textContent = `${student}`;

            // pUniversity;
            const pUniversity = document.createElement('p');
            pUniversity.textContent = `University: ${university}`;

            // pScore;
            const pScore = document.createElement('p');
            pScore.textContent = `Score: ${score}`;

            // pContainer & Append h4 and p's;
            const pContainer = document.createElement('article');
            pContainer.appendChild(h4Name);
            pContainer.appendChild(pUniversity);
            pContainer.appendChild(pScore);

            // applicationContainer
            const applicationContainer = document.createElement('li');
            applicationContainer.className = 'application';
            applicationContainer.appendChild(pContainer);
            applicationContainer.appendChild(editButton);
            applicationContainer.appendChild(applyButton);

            // Append applicationContainer to previewList;
            previewList.appendChild(applicationContainer);

            // Disable nextButton;
            nextButton.disabled = true;

            // Clear input fields;
            studentInput.value = '';
            universityInput.value = '';
            scoreInput.value = '';

            // editButton addEventListener;
            editButton.addEventListener('click', () => {
                // Fill input fields;
                studentInput.value = student;
                universityInput.value = university;
                scoreInput.value = score;

                // Enable nextButton;
                nextButton.disabled = false;

                // Remove applicationContainer from previewList;
                applicationContainer.remove();
            })

            // applyButton addEventListener;
            applyButton.addEventListener('click', () => {
                // Remove editButton and applyButton;
                editButton.remove();
                applyButton.remove()

                // Append applicationContainer to candidatesList;
                candidatesList.appendChild(applicationContainer)

                // Clear previewList;
                previewList.innerHTML = '';

                // Enable nextButton;
                nextButton.disabled = false;
            })
        }
    });
}