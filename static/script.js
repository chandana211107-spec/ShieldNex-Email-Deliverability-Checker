async function checkEmails() {

    const input = document.getElementById("emails");
    const resultsDiv = document.getElementById("results");
    const loading = document.getElementById("loading");
    const summary = document.getElementById("summary");
    const button = document.getElementById("checkButton");

    const emails = input.value
        .split("\n")
        .map(email => email.trim())
        .filter(email => email !== "");


    // Check whether user entered anything

    if (emails.length === 0) {

        resultsDiv.innerHTML =
            '<p class="error">Please enter at least one email address.</p>';

        summary.classList.add("hidden");

        return;
    }


    // Show loading

    loading.style.display = "block";
    button.disabled = true;
    resultsDiv.innerHTML = "";


    try {

        const response = await fetch("/check", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                emails: emails
            })

        });


        const results = await response.json();


        // Count results

        let deliveredCount = 0;
        let bounceCount = 0;
        let unknownCount = 0;


        results.forEach(result => {

            if (result.status === "Likely to be delivered") {
                deliveredCount++;
            }

            else if (result.status === "Likely to bounce") {
                bounceCount++;
            }

            else {
                unknownCount++;
            }

        });


        // Update summary

        document.getElementById("deliveredCount").textContent =
            deliveredCount;

        document.getElementById("bounceCount").textContent =
            bounceCount;

        document.getElementById("unknownCount").textContent =
            unknownCount;

        summary.classList.remove("hidden");


        // Create results table

        let table = `
            <table>

                <thead>

                    <tr>
                        <th>Email Address</th>
                        <th>Status</th>
                        <th>Reason</th>
                    </tr>

                </thead>

                <tbody>
        `;


        results.forEach(result => {

            let statusClass = "unknown";


            if (result.status === "Likely to be delivered") {

                statusClass = "delivered";

            }

            else if (result.status === "Likely to bounce") {

                statusClass = "bounce";

            }


            table += `
                <tr>

                    <td>
                        ${result.email}
                    </td>

                    <td class="status ${statusClass}">
                        ${result.status}
                    </td>

                    <td>
                        ${result.reason}
                    </td>

                </tr>
            `;

        });


        table += `
                </tbody>

            </table>
        `;


        resultsDiv.innerHTML = table;


    }

    catch (error) {

        resultsDiv.innerHTML =
            '<p class="error">Unable to connect to the server. Please try again.</p>';

    }


    finally {

        loading.style.display = "none";
        button.disabled = false;

    }

}