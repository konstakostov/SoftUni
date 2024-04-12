window.addEventListener("load", solve);

function solve() {
    const titleInput = document.getElementById('task-title');
    const categoryInput = document.getElementById('task-category');
    const contentInput = document.getElementById('task-content');

    const reviewList = document.getElementById('review-list');
    const publishedList = document.getElementById('published-list');


    const publishButton = document.getElementById('publish-btn')
    publishButton.addEventListener('click', () => {
        const title = titleInput.value;
        const category = categoryInput.value;
        const content = contentInput.value;

        if (title !== '' && category !== '' && content !== '') {
            // editButton;
            const editButton = document.createElement('button');
            editButton.className = 'action-btn edit';
            editButton.textContent = 'Edit';

            // postButton;
            const postButton = document.createElement('button');
            postButton.className = 'action-btn post';
            postButton.textContent = 'Post';

            // h4Title;
            const h4Title = document.createElement('h4');
            h4Title.textContent = title;

            // pCategory;
            const pCategory = document.createElement('p');
            pCategory.textContent = `Category: ${category}`;

            // pContent;
            const pContent = document.createElement('p');
            pContent.textContent = `Content: ${content}`;

            // articleContainer & append h4Title, pCategory, pContent;
            const articleContainer = document.createElement('article');
            articleContainer.appendChild(h4Title);
            articleContainer.appendChild(pCategory);
            articleContainer.appendChild(pContent);

            // rPost & Append buttons articleContainer;
            const rPost = document.createElement('li');
            rPost.classList.add('rpost');
            rPost.appendChild(articleContainer);
            rPost.appendChild(editButton);
            rPost.appendChild(postButton);

            // Append rPost to reviewList;
            reviewList.appendChild(rPost);

            // Clear input fields;
            clearInputFields();

            // editButton addEventListener;
            editButton.addEventListener('click', () => {
                // Fill input fields;
                titleInput.value = title;
                categoryInput.value = category;
                contentInput.value = content;

                // Remove rPost;
                rPost.remove();
            })

            // okButton addEventListener;
            postButton.addEventListener('click', () => {
                // Remove editButton and okButton
                editButton.remove()
                postButton.remove()


                // Append rPost to publishedList;
                publishedList.appendChild(rPost);

                // Clear reviewList children elements;
                reviewList.innerHTML = ''
            })
        }
    })

    function clearInputFields() {
        titleInput.value = '';
        categoryInput.value = '';
        contentInput.value = '';
    }
}