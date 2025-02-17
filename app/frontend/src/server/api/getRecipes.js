export default defineEventHandler(async (event) => {
    if (event.req.method !== "GET") {
        return { status: "error", message: "Invalid request method" };
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/recipes", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (response.ok) {
            const recipes = await response.json();
            console.log("Recipes:", recipes);
            return { status: "success", recipes };
        } else {
            console.error("Error retrieving recipes!");
            return { status: "error", message: "Error retrieving recipes!" };
        }
    } catch (error) {
        console.error("Error:", error);
        return { status: "error", message: "Failed to connect to server!" };
    }
});
