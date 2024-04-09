function attachEvents() {
    const postsURL = 'http://localhost:3030/jsonstore/blog/posts';
    const commentsURL = 'http://localhost:3030/jsonstore/blog/comments';

    const loadPostsButton = document.getElementById('btnLoadPosts');
    loadPostsButton.addEventListener('click', loadPostsEvent);

    const postsSelect = document.getElementById('posts');

    const viewPostButton = document.getElementById('btnViewPost');
    viewPostButton.addEventListener('click', viewPostEvent);

    let allPosts = {};

    async function loadPostsEvent(event) {
        postsSelect.innerHTML = '';
        const allPostsResponse = await fetch(postsURL);
        allPosts = await allPostsResponse.json();

        for (let [postId, post] of Object.entries(allPosts)) {
            const option = document.createElement('option');
            option.textContent = post.title;
            option.value = postId;
            postsSelect.appendChild(option);
        }
    }

    async function viewPostEvent(event) {
        const currentPostObject = document.getElementById('posts');
        const currentPostComments = [];

        const allCommentsResponse = await fetch(commentsURL);
        const allComments = await allCommentsResponse.json();

        for (let [commentId, comment] of Object.entries(allComments)) {
            if (comment.postId === currentPostObject.value) {
                currentPostComments.push(comment.text);
            }
        }

        const chosenPost = allPosts[currentPostObject.value];

        const titleElement = document.getElementById('post-title');
        titleElement.textContent = chosenPost.title;

        const postContentElement = document.getElementById('post-body');
        postContentElement.textContent = chosenPost.body;

        const ul = document.getElementById('post-comments');
        ul.innerHTML = '';
        for (let comment of currentPostComments) {
            const li = document.createElement('li');
            li.textContent = comment;
            ul.appendChild(li);
        }
    }
}

attachEvents();
