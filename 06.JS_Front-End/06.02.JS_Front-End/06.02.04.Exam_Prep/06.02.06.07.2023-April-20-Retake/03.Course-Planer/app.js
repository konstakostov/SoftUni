const baseURL = 'http://localhost:3030/jsonstore/tasks'

let currentCourseID = null;

const courseNameInput = document.getElementById('course-name');
const courseTypeInput = document.getElementById('course-type');
const descriptionInput = document.getElementById('description');
const teacherNameInput = document.getElementById('teacher-name');

const coursesList = document.getElementById('list');

const addButton = document.getElementById('add-course');
addButton.addEventListener('click', async () => {
    // Create POST request;
    const response = await fetch(baseURL, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            title: courseNameInput.value,
            type: courseTypeInput.value,
            description: descriptionInput.value,
            teacher: teacherNameInput.value,
        }),
    });

    // Check if POST request is valid;
    if (!response.ok) {
        return;
    }

    // Clear input fields;
    clearInputFields();

    // Load Courses;
    await loadCoursesFunctionality();
})

const editCourseButton = document.getElementById('edit-course');
editCourseButton.addEventListener('click', async () => {
    // Make PUT request;
    const response = await fetch(`${baseURL}/${currentCourseID}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            title: courseNameInput.value,
            type: courseTypeInput.value,
            description: descriptionInput.value,
            teacher: teacherNameInput.value,
            _id: currentCourseID,
        })
    });

    // Check if PUT request is valid;
    if (!response.ok) {
        return;
    }

    // Deactivate editCourseButton;
    editCourseButton.disabled = true;

    // Activate addButton;
    addButton.disabled = false;

    // Clear the input fields;
    clearInputFields();

    // Clear currentMealID;
    currentCourseID = null;

    // Load Meals;
    await loadCoursesFunctionality();
})

const loadCourses = document.getElementById('load-course');
loadCourses.addEventListener('click', loadCoursesFunctionality);

async function loadCoursesFunctionality() {
    // Fetch all records;
    const response = await fetch(baseURL);
    const data = await response.json();

    // Clear coursesList element;
    coursesList.innerHTML = '';

    // Create a course element for every object in data;
    for (const course of Object.values(data)) {
        // finishButton;
        const finishButton = document.createElement('button');
        finishButton.classList.add('finish-btn');
        finishButton.textContent = 'Finish Course';

        // editButton;
        const editButton = document.createElement('button');
        editButton.classList.add('edit-btn');
        editButton.textContent = 'Edit Course';

        // h4Description;
        const h4Description = document.createElement('h4');
        h4Description.textContent = course.description;

        // h3CourseType;
        const h3CourseType = document.createElement('h3');
        h3CourseType.textContent = course.type;

        // h3teacherName;
        const h3teacherName = document.createElement('h3')
        h3teacherName.textContent = course.teacher;

        // h2CourseName;
        const h2CourseName = document.createElement('h2');
        h2CourseName.textContent = course.title;

        // courseContainer;
        const courseContainer = document.createElement('div');
        courseContainer.classList.add('container');
        courseContainer.appendChild(h2CourseName);
        courseContainer.appendChild(h3teacherName);
        courseContainer.appendChild(h3CourseType);
        courseContainer.appendChild(h4Description);
        courseContainer.appendChild(editButton);
        courseContainer.appendChild(finishButton);

        // Append courseContainer to coursesList;
        coursesList.appendChild(courseContainer);

        // Disable editCourseButton;
        editCourseButton.disabled = true;

        // editButton addEventListener;
        editButton.addEventListener('click', () => {
            // Get current course ID;
            currentCourseID = course._id;

            // Get courses data & Populate input fields;
            descriptionInput.value = course.description;
            courseTypeInput.value = course.type;
            teacherNameInput.value = course.teacher;
            courseNameInput.value = course.title;

            // Activate editCourseButton;
            editCourseButton.disabled = false;

            // Deactivate addButton;
            addButton.disabled = true;

            // Remove courseContainer from coursesList;
            courseContainer.remove();
        })

        // deleteButton addEventListener;
        finishButton.addEventListener('click', async () => {
            // Create DELETE request;
            await fetch(`${baseURL}/${course._id}`, {
                method: 'DELETE',
            })

            // Check if DELETE request is valid;
            if (!response.ok) {
                return;
            }

            // Remove courseContainer from coursesList;
            courseContainer.remove();
        })
    }
}

function clearInputFields() {
    courseNameInput.value = '';
    courseTypeInput.value = '';
    descriptionInput.value = '';
    teacherNameInput.value = '';
}