"use server"

export async function registration(formData: FormData) {
    const email = formData.get("email");
    const password = formData.get("password");
    const passwordRepeat = formData.get("passwordrepeat");
    const username = formData.get("username");

    // Here you would typically handle the signup logic, such as saving the user to a database
    // For demonstration purposes, we'll just log the email and password
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Username:", username);
    console.log("Password Repeat:", passwordRepeat);

    // Return a response or redirect as needed
    return { success: true, message: "Registration successful!" };
    // This function is a server action for handling user signup

}