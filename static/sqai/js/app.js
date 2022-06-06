const contactForm = document.querySelector('#contactForm');

const name = document.querySelector('#name');
const email = document.querySelector('#email');
const subject = document.querySelector('#subject');
const message = document.querySelector('#message');


contactForm.addEventListener('submit', (e) => {
    e.preventDefault();

    let formData = {
        name: name.value,
        email: email.value,
        subjecct: subject.value,
        message: message.value
    };

    let req = new XMLHttpRequest();
    req.open('POST', '/contact');
    req.setRequestHeader('content-type', 'application/json')
    req.onload = function () {

        if (req.responseText == 'success') {
            name.value = '',
                email.value = '',
                subject.value = '',
                message.value = ''
        } else {
            alert('Something went wrong');
        }
    }

    req.send(JSON.stringify(formData));
});

