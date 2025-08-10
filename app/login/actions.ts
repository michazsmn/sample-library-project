"use server"

export async function signup(formData: FormData) {
  // This function is a server action for handling user signup
  const email = formData.get("email");
  const password = formData.get("password");

  await fetch('http://127.0.0.1:8000/auth/token', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        email: email,
        password: password,
    }),
  });

  return { success: true, message: "Signup successful!" };
}
