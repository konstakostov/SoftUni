function toggle() {
    const moreButtonElement = document.getElementsByClassName('button')[0];
    const extraTextElement = document.getElementById('extra');

    const moreButtonLabel = moreButtonElement.textContent;

    if (moreButtonLabel === 'More') {
        moreButtonElement.textContent = 'Less';
        extraTextElement.style.display = 'block';
    } else {
        moreButtonElement.textContent = 'More';
        extraTextElement.style.display = 'none';
    }
}