document.addEventListener("DOMContentLoaded", function () {
    if (typeof pdfjsLib === "undefined") {
        console.error("PDF.js is not loaded! Check the script path.");
        return;
    }

    const canvas = document.getElementById("pdf-canvas");
    const pdfUrl = canvas.dataset.pdf;
    let pdfDoc = null;
    let currentPage = 1;
    const scale = 0.9; // Adjust the scale for better visibility

    // Configure PDF.js worker
    pdfjsLib.GlobalWorkerOptions.workerSrc =
        "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.10.111/pdf.worker.min.js";

    // Function to render a page
    function renderPage(pageNumber) {
        pdfDoc.getPage(pageNumber).then((page) => {
        const viewport = page.getViewport({ scale });
        const context = canvas.getContext("2d");
        
        canvas.width = viewport.width;
        canvas.height = 600;

        const renderContext = {
            canvasContext: context,
            viewport: viewport,
        };

        page.render(renderContext);
        document.getElementById("page-num").textContent = `Page ${currentPage} of ${pdfDoc.numPages}`;
        });
    }

    // Load the PDF
    pdfjsLib.getDocument(pdfUrl).promise.then((pdf) => {
        pdfDoc = pdf;
        renderPage(currentPage);
    });

    // Event Listeners for Next and Previous Buttons
    document.getElementById("prev-page").addEventListener("click", () => {
        if (currentPage > 1) {
        currentPage--;
        renderPage(currentPage);
        }
    });

    document.getElementById("next-page").addEventListener("click", () => {
        if (currentPage < pdfDoc.numPages) {
        currentPage++;
        renderPage(currentPage);
        }
    });
});
