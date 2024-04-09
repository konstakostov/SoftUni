function attachEvents() {
    const urlPost = 'http://localhost:3030/jsonstore/blog/posts';
    const urlComments = 'http://localhost:3030/jsonstore/blog/comments';

    const loadPostsButtonElement = document.getElementById('btnLoadPosts');
    const viewPostsButtonElement = document.getElementById('btnViewPost');
    const selectPostElement = document.getElementById('posts');
    const postBodyElement = document.getElementById('post-body');
    const commentListElement = document.getElementById('post-comments');
    const postTitleElement = document.getElementById('post-title');

    loadPostsButtonElement.addEventListener('click', () => {
        selectPostElement.innerHTML = '';

        fetch(urlPost)
            .then(response => response.json())
            .then(posts => {
                Object.values(posts)
                    .forEach(post => {
                        const optionElement = document.createElement('option');
                        optionElement.value = post.id;
                        optionElement.textContent = post.title;

                        selectPostElement.appendChild(optionElement)
                    })
            });
    });

    viewPostsButtonElement.addEventListener('click', async () => {
        const selectedPostId = selectPostElement.value;

        const response = await fetch(`${urlPost}/${selectedPostId}`);
        const selectedPost = await response.json();

        postBodyElement.textContent = selectedPost.body;
        postTitleElement.textContent = selectedPost.title

        const commentsResponse = await fetch(urlComments);
        const comments = await commentsResponse.json();

        Object.values(comments)
            .filter(comment => comment.postId === selectedPostId)
            .map(comment => {
                const liElement = document.createElement('li');
                liElement.id = comment.id;
                liElement.textContent = comment.text;

                commentListElement.innerHTML = '';
                commentListElement.appendChild(liElement);
            });

    })
}

attachEvents();