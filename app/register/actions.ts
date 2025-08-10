"use server"

export async function registration(formData: FormData) {
    const email = formData.get("email");
    const password = formData.get("password");
    const passwordRepeat = formData.get("passwordrepeat");
    const username = formData.get("username");

    if (password !== passwordRepeat) {
        throw new Error("Passwords do not match");
    } else {
        
    await fetch('http://127.0.0.1:8000/auth/register', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password,
            username: username,
        }),
    });

    return { success: true, message: "Registration successful!" };
    }
}