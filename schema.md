# Database Collections

## `users`

*   `id` (integer)
*   `name` (string)
*   `register_date` (date)
*   `last_login_time` (datetime)
*   `distance` (integer)
*   `exploration` (integer)

## `routes`

*   `id` (integer)
*   `user_id` (integer)
*   `popularpath_id` (integer, optional)
*   `date` (date)
*   `start_id` (integer)
*   `end_id` (integer)
*   `distance` (integer, in meters)
*   `disqualified` (boolean)
*   `efficiency` (integer, 0–100)
*   `time` (integer, in seconds)

## `waypoints`

*   `id` (integer)
*   `user_id` (integer)
*   `route_id` (integer)
*   `name` (string)
*   `date` (date)
*   `latitude` (float)
*   `longitude` (float)
*   `accuracy` (integer?)

## `popularpaths`

*   `pid` (integer)
*   `wids` (list of integers)

## `sessions`

*   `uid` (integer)
*   `uuid` (string?)
*   `time` (datetime)
