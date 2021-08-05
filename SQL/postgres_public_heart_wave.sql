create table heart_wave
(
    heart_wave double precision[],
    dog_id     integer
        constraint heart_wave_dog_id_fkey
            references dogs,
    time       timestamp
);

alter table heart_wave
    owner to apple;

