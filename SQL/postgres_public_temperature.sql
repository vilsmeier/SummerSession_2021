create table temperature
(
    temperature double precision,
    dog_id      integer
        constraint temperature_dog_id_fkey
            references dogs,
    time        timestamp
);

alter table temperature
    owner to apple;

