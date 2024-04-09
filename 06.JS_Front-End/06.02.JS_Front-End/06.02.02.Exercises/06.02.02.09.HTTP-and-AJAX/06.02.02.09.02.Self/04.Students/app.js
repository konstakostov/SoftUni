function attachEvents() {
    const baseURL = 'http://localhost:3030/jsonstore/collections/students';

    const tbElement = document.querySelector('tbody');

    const submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', submitButtonFunctionality)

    async function extractStudents() {
        tbElement.innerHTML = '';

        const studentsResponse = await fetch(baseURL);
        const students = await studentsResponse.json();

        Object
            .keys(students)
            .forEach(student => {
                const studentData = students[student];

                const tdFirstNameElement = document.createElement('td');
                tdFirstNameElement.textContent = studentData.firstName;

                const tdLastNameElement = document.createElement('td');
                tdLastNameElement.textContent = studentData.lastName;

                const tdFacultyNumberElement = document.createElement('td');
                tdFacultyNumberElement.textContent = studentData.facultyNumber;

                const tdGradeElement = document.createElement('td');
                tdGradeElement.textContent = studentData.grade;

                const trElement = document.createElement('tr');
                trElement.appendChild(tdFirstNameElement);
                trElement.appendChild(tdLastNameElement);
                trElement.appendChild(tdFacultyNumberElement);
                trElement.appendChild(tdGradeElement);

                tbElement.appendChild(trElement);
            })
    }

    extractStudents();

    async function submitButtonFunctionality() {
        const firstName = document.querySelector('input[name=firstName]');
        const lastName = document.querySelector('input[name=lastName]');
        const facultyNumber = document.querySelector('input[name=facultyNumber]');
        const grade = document.querySelector('input[name=grade]');

        const student = {
            firstName: firstName.value,
            lastName: lastName.value,
            facultyNumber: facultyNumber.value,
            grade: grade.value,
        }

        await fetch(baseURL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(student),
        })

        extractStudents()

        firstName.value = '';
        lastName.value = '';
        facultyNumber.value = '';
        grade.value = '';
    }
}

attachEvents();