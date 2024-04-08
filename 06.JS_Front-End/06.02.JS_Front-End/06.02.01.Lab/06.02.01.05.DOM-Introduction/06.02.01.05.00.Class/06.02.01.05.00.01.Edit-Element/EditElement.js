function editElement(reference, match, replacer) {
    // // This does NOT work in Judge;
    // const currentContent = reference.textContent.replaceAll(match, replacer);

    // // RegEx solution;
    // reference.textContent = reference.textContent.replace(new RegExp(match, 'g'), replacer);

    while (reference.textContent.includes(match)) {
        reference.textContent = reference.textContent.replace(match, replacer);
    }
}