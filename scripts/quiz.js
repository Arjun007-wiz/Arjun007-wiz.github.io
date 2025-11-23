// Simple client-side quiz logic. Update the answers here to match About page content.
const answers = {
  q1: 'example-location', // replace with the correct short answer (lowercase)
  q2: 'programming', // replace with a hobby listed in about.html (lowercase)
  q3: 'true'
};

document.getElementById('quiz-form').addEventListener('submit', function(e){
  e.preventDefault();
  const form = e.target;
  const r = document.getElementById('result');
  const q1 = (form.q1.value || '').trim().toLowerCase();
  const q2 = (form.q2.value || '').trim().toLowerCase();
  const q3 = (form.q3.value || '').trim().toLowerCase();

  let score = 0;
  if(q1 === answers.q1) score++;
  if(q2 === answers.q2) score++;
  if(q3 === answers.q3) score++;

  r.textContent = `You scored ${score} / 3.`;
  if(score === 3){
    r.textContent += ' 🎉 All correct — claim your prize! (Add prize details in the repo)';
  }
});
