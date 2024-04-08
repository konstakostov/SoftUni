function solve(grade) {
    let gradeWords = '';
    let gradeNumber = 0;

    if (grade < 3.00) {
        gradeWords = 'Fail';
        gradeNumber = 2;
    } else if (grade >= 3.00 && grade < 3.50) {
        gradeWords = 'Poor';
        gradeNumber = grade.toFixed(2);
    } else if (grade >= 3.50 && grade < 4.50) {
        gradeWords = 'Good';
        gradeNumber = grade.toFixed(2);
    } else if (grade >= 4.50 && grade < 5.50) {
        gradeWords = 'Very good';
        gradeNumber = grade.toFixed(2);
    } else if (grade <= 5.50) {
        gradeWords = 'Excellent';
        gradeNumber = grade.toFixed(2);
    }

    console.log(`${gradeWords} (${gradeNumber})`);
}

solve(3.33);
solve(4.50);
solve(2.99);