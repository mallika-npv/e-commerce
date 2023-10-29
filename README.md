# Auction Website

Welcome to our Auction Website, a platform where users can create, explore, bid on, and manage auction listings. This document provides an overview of the features and functionalities of our web application.

## Table of Contents
1. [Create Listing](#create-listing)
2. [Active Listings Page](#active-listings-page)
3. [Listing Page](#listing-page)
4. [Watchlist](#watchlist)

## Create Listing

Users can visit the "Create Listing" page to create a new auction listing. When creating a listing, users are required to provide the following information:

- **Title**: A title for the listing.
- **Description**: A detailed text-based description of the item being listed.
- **Starting Bid**: The initial bid amount for the auction.
- **Optional Fields**:
  - **Image URL**: Users can provide a URL for an image related to the listing.
  - **Category**: Users can specify a category for the listing (e.g., Fashion, Toys, Electronics, Home, etc.).

## Active Listings Page
The default route of the web application allows users to view all currently active auction listings. For each active listing, the following information is displayed:
- **Title**: Title of the listing.
- **Description**: Description of the item being auctioned.
- **Current Price**: The current highest bid for the listing.
- **Photo**: An image representing the listing (if provided by the seller).

## Listing Page
Clicking on a listing takes users to a specific page dedicated to that listing. On this page, users can view the following details:
- **Title**: Title of the listing.
- **Description**: Detailed description of the item being auctioned.
- **Current Price**: The current highest bid for the listing.
- **Image**: Image representing the listing (if provided).
- **Watchlist**: Signed-in users can add or remove the item from their watchlist.
- **Bidding**: Signed-in users can place bids on the item, provided the bid meets the criteria (at least as large as the starting bid and greater than any other bids placed).
- **Comments**: Users can add comments to the listing page, and all comments made on the listing are displayed.

## Watchlist
Signed-in users can access the "Watchlist" page, which displays all the listings they have added to their watchlist. Clicking on any of these listings takes the user to the specific listing page, allowing them to participate in the auction or view the details of the item.
