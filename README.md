# FitnessTracker
A fitness tracker based on data from Apple Health &amp; Fitness

## Project Goal
As someone who has quietly found themself getting obsessed with running (again), I want to create an app that improves on the 'Health' iPhone app. I personally get a kick out of seeing the lines going up (or down) when I am working hard, to give me validation that it is paying off.

My first goal is to solely work on the vo2 max data visualisation as this is my primary metric. The data will be sent to my Django API and automatically update my app.

### (Currently working on) Data Visualisation Goals:
- Allow for goal-setting over weeks, months, years
- Show more details on fitness levels with levels displayed on graphs
- Have the graphs be dynamic and scrollable
- Display personal levels on graph (high/low/average for all-time, seasonal, training block, moving averages, projections etc.)

### Potential Goals further on:
- Expand the vo2 max graphs to my other favoured metrics - resting HR, steps etc.
- Allow for friends to use the app so we can track each other, compete relative to our level - for example race to improve metric x by y in z weeks.
- Add feature to analyse gpx files to go more in depth on runs (or equivalent) much like strava does but without a paywall.
  
## API & Apple Data Pain
The first issue is getting the data from Apple. Luckily someone has created an app for this - called [Health Auto Export - JSON+CSV](https://apps.apple.com/gb/app/health-auto-export-json-csv/id1115567069). This allows for automatic exporting of data to our API.

I have never created an API before so this has been a struggle but it seems to be working currently. 

