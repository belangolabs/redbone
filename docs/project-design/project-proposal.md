# Project Proposal

A multi-platform social media feature store for easy querying and analysis.

## Overview
Collects streaming data and prepares it for entry into a feature store

This project will pull in multiple streaming sources, store them, and make them available for integrated analysis.

### What will not be included in this project
This project does not currently address the analysis on said social media.
This project may or may not include a visual UI. Even if it does right now, it is conceivable that this would get moved later.

## Report Types

### Engagement Report 
* how frequently is each keyword or usertag being mentioned?
* what is the general sentiment behind each of these?
* generate samples from across the sentiment pool, or community pool
* who is engaging with these keywords or user
    * keyword engagement means general usage of term
    * user engagement means responding to, following, etc.

#### Open questions
1. What about other types of multi-post items, e.g. songs, images, phrases?

### Response Report
* response to a specific post
  * engagement, sentiment, etc.
  * any cross-communications (e.g. threaded comments) of note
* summaries of responses

#### Open questions
1. Should we provide aggregate responses for all posts? should that be an optional, always included, or never?


### Longitudinal Analysis Report
* how has engagement changed over time
* how static or not is the community pool

### Trending Report
* broad analysis of what is currently trending


## Tentative Data Sources

1. TikTok
Twitter
Telegram
YouTube