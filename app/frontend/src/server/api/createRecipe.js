export default defineEventHandler(async (event) => {
  if (event.req.method !== "POST") {
      return { status: "error", message: "Invalid request method" };
  }

  try {
      const body = await readBody(event); // Read request body
      const response = await fetch("http://127.0.0.1:8000/create_recipe", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify(body),
      });

      if (response.ok) {
          return { status: "success", message: "Recipe submitted successfully!" };
      } else {
          return { status: "error", message: "Error submitting recipe!" };
      }
  } catch (error) {
      console.error("Error:", error);
      return { status: "error", message: "Failed to connect to server!" };
  }
});
