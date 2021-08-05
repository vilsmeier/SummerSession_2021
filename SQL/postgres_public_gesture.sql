create table gesture
(
    gesture varchar,
    dog_id  integer
        constraint gesture_dog_id_fkey
            references dogs,
    time    timestamp
);

alter table gesture
    owner to apple;

