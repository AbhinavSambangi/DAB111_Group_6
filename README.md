Group_6_Python/

├── data_preprocessing/       # Notebook and raw data
│   ├── load_data.ipynb       # Jupyter notebook to clean and insert data into the database
│   └── nft_sales.csv         # Raw NFT sales CSV file
│
├── database/
│   └── nft.db                # Final SQLite database used by the Flask app
│
├── website/                  # Flask web application
│   ├── app.py                # Main Flask backend logic
│   └── templates/            # HTML templates used for rendering UI
│       ├── index.html        # Landing page with buttons
│       ├── nft_data.html     # Full NFT sales data in table form
│       └── nft_names.html    # List of NFT collections in table form
├── requirements.txt      # Required Python packages (Flask, pandas, sqlite3, os)
