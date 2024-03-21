const usernameField = document.querySelector('#usernameField');
const emailFeild = document.querySelector('#emailFeild');
const feedbackArea = document.querySelector('.invalid-feedback');
const emailFeedBackArea = document.querySelector('.emailFeedBackArea');
const showPassword = document.querySelector('.showPassword');
const passwordField = document.querySelector('#passwordField');
const submitBtn = document.querySelector('.submit-btn');
const passwordlen = document.querySelector('#passwordField');
const passwordlength = document.querySelector('.passwordlen');

passwordlen.addEventListener('keyup', (e) => {
    console.log('88',88);
    passwordlength.style.display = 'none';
    const passwordVal = e.target.value;
    if (passwordVal.length < 6) {
        passwordlength.style.display = 'block';
        passwordlength.innerHTML = `<p style="font-size: 12px;">Password must be at least 6 characters</p>`;
    } else {
        showPassword.style.display = 'block';
    }
});



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
                submitBtn.disabled = true;
                usernameField.classList.add('is-invalid');
                feedbackArea.style.display = 'block';
                feedbackArea.innerHTML = `<p style="font-size: 9px;">${data.username_error}</p>`;
            } else {
                submitBtn.removeAttribute('disabled');
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
                submitBtn.disabled = true;
                emailFeild.classList.add('is-invalid');
                emailFeedBackArea.style.display = 'block';
                emailFeedBackArea.innerHTML = `<p style="font-size: 12px;">${data.email_error}</p>`;
            } else {
                submitBtn.removeAttribute('disabled');
            }   
        });
    }
});