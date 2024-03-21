const usernameField = document.querySelector('#usernameField');
const emailFeild = document.querySelector('#emailFeild');
const feedbackArea = document.querySelector('.invalid-feedback');
const emailFeedBackArea = document.querySelector('.emailFeedBackArea');
const showPassword = document.querySelector('.showPassword');
const passwordField = document.querySelector('#passwordField');

showPassword.addEventListener('click', (e) => {
    if (showPassword.textContent === 'Show Password') {
        showPassword.textContent = 'Hide Password';
        passwordField.setAttribute('type', 'text');
    } else {
        showPassword.textContent = 'Show Password';
        passwordField.setAttribute('type', 'password');
    }


});

usernameField.addEventListener('keyup', (e) => {
    console.log('88',88);
    const usernameVal = e.target.value;
    usernameField.classList.remove('is-invalid');
    feedbackArea.style.display = 'none';
    if (usernameVal.length > 0) {
        fetch('/authentication/validate_username', {
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if (data.username_error) {
                usernameField.classList.add('is-invalid');
                feedbackArea.style.display = 'block';
                feedbackArea.innerHTML = `<p style="font-size: 9px;">${data.username_error}</p>`;
            }
        });
    }
});

emailFeild.addEventListener("keyup", (f) => {
    const emailVal = f.target.value;
    console.log('88',88);
    
    emailFeild.classList.remove("is-invalid");
    emailFeedBackArea.style.display = "none";
    if (emailVal.length > 0) {
        fetch('/authentication/validate-email', {
            body: JSON.stringify({email: emailVal}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if (data.email_error) {
                emailFeild.classList.add('is-invalid');
                emailFeedBackArea.style.display = 'block';
                emailFeedBackArea.innerHTML = `<p style="font-size: 12px;">${data.email_error}</p>`;
            } 
        });
    }
});