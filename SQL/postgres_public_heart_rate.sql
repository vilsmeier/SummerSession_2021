create table heart_rate
(
    heart_rate integer,
    dog_id     integer
        constraint heart_rate_dog_id_fkey
            references dogs,
    time       timestamp
);

alter table heart_rate
    owner to apple;

