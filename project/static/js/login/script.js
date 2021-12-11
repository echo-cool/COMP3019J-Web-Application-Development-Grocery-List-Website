$('#sign_up').click(function () {
    $('.login-move_box').css('transform', 'translateX(80%)');
    $('.sign_in').addClass('login-hidden');
    $('.sign_up').removeClass('login-hidden');
});

$('#sign_in').click(function () {
    $('.login-move_box').css('transform', 'translateX(0%)');
    $('.sign_up').addClass('login-hidden');
    $('.sign_in').removeClass('login-hidden');
});
const csrf_token = $("meta[name=csrf-token]").attr("content");

function validateEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function validateUsername(username) {
    const re = /^[a-zA-Z0-9]{5,20}$/;
    return re.test(String(username).toLowerCase());
}

function validatePassword(password) {
    const re = /^[a-zA-Z0-9]{5,20}$/;
    return re.test(String(password).toLowerCase());
}


function checkEmail(email) {
    let message = $("#register-email-input-message");
    if (validateEmail(email)) {
        message.text("");
        $.ajax({
            url: '/check/email',
            type: 'POST',
            data: {
                "email": email,
                "csrf_token": csrf_token
            },
            success: function (data) {
                if (data == "true") {
                    message.text("Email is available");
                    message.css("color", "green");
                } else {
                    message.text("Email is not available");
                    message.css("color", "red");
                }
            }
        });
    } else {
        message.text("Email is invalid");
        message.css("color", "red");
    }
}

function checkUsername(username, is_sign_up) {
    let message = $("#login-username-input-message");
    if (is_sign_up) {
        message = $("#register-username-input-message");
    } else {
        message = $("#login-username-input-message");
    }

    if (validateUsername(username)) {
        if (is_sign_up) {
            $.ajax({
                url: '/check/username',
                type: 'POST',
                data: {
                    "username": username,
                    "csrf_token": csrf_token
                },
                success: function (data) {
                    if (data == "true") {
                        message.text("Username is available");
                        message.css("color", "green");
                    } else {
                        message.text("Username is not available");
                        message.css("color", "red");
                    }
                }
            });
        }
        message.text("");
    } else {
        message.text("Username must be 5-20 characters long and contain only letters and numbers");
        message.css("color", "red");
    }
}

function checkPassword(val, is_sign_up) {
    let message = $("#login-password-input-message");
    if (is_sign_up)
        message = $("#register-password-input-message");
    else
        message = $("#login-password-input-message");
    let password1 = $("#register-password-input-text").val();
    let password2 = $("#register-password-confirm-input-text").val();
    if (is_sign_up) {
        val = password1;
    }
    if (validatePassword(val)) {
        message.text("");

        console.log(password1);
        console.log(password2)
        if (is_sign_up) {
            if (password1 == password2) {
                message.text("");
            } else {
                message.text("Passwords do not match");
                message.css("color", "red");
            }
        }
    } else {
        message.text("Password must be at least 5 characters long.");
        message.css("color", "red");
    }

}

$(document).ready(function () {
    $("#login-username-input-text").on("input", function () {
        checkUsername($(this).val(), false);
    });

    $("#login-password-input-text").on("input", function () {
        checkPassword($(this).val(), false);
    });
    $("#register-username-input-text").on("input", function () {
        checkUsername($(this).val(), true);
    });

    $("#register-email-input-text").on("input", function () {
        checkEmail($(this).val());
    });

    $("#register-password-input-text").on("input", function () {
        checkPassword($(this).val(), true);
    });
    $("#register-password-confirm-input-text").on("input", function () {
        checkPassword($(this).val(), true);
    });

});



