# Web Scraping with Scrapy - Navodesk

## Overview
This Scrapy spider (`navo`) extracts product information from the Navodesk website, including details like SKU, cost, color, dimensions, weight, and more. The spider utilizes Scrapy for web scraping, and the extracted data is organized and exported in JSON format.

## Features
- **Dynamic URL Generation:** The spider dynamically generates URLs for different pages of the Navodesk website.
- **Data Extraction:** Extracts product URLs from each page and then retrieves detailed information for each product.
- **Data Fields:** Extracted fields include SKU, cost, color, dimensions, weight, title, URL, review count, product detail, return policy, date and time, and brand name.
- **Handling Variations:** Handles product variations, such as different colors, and extracts relevant information.

## How to Run
1. **Install Scrapy:** Ensure Scrapy is installed. If not, run `pip install scrapy` in your terminal.
2. **Run the Spider:** Navigate to the project directory and run the spider using the command `scrapy crawl navo -o output.json`.
3. **View Results:** Open the generated `output.json` file to view the extracted data.

## Spider Logic
- The spider starts by generating URLs for multiple pages of the Navodesk website.
- It then extracts product URLs from each page.
- For each product URL, it extracts detailed information such as SKU, cost, color, dimensions, weight, title, URL, review count, product detail, return policy, date and time, and brand name.
- The spider handles variations in product color, providing a comprehensive dataset.

## JSON Output
```json
[
    {
        "maximum": "quantity",
        "sku": "product_sku",
        "Cost": "product_cost_str",
        "Color": "product_colour_arr[plus]",
        "length": null,
        "width": null,
        "height": null,
        "weight": "weight_sum",
        "title": "title",
        "url": "url",
        "review": "review",
        "Product detail": "product_detail",
        "Return Policy": "return_policy",
        "Date and Time": "today",
        "Brand": "brand"
    },
    // ... (additional product entries)
]
```

## Notes
- The spider dynamically handles the presence or absence of product variations in the source code.
- The output is structured to provide flexibility for different product scenarios.

Feel free to customize the spider or enhance its features based on specific requirements. If you encounter any issues or have suggestions, please refer to the project's documentation or reach out to the project maintainers. Happy scraping!
