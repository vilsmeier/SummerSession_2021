create table motion
(
    latitude   double precision,
    altitude   double precision,
    velocity   double precision,
    accelerate double precision,
    direction  double precision,
    dog_id     integer
        constraint motion_dog_id_fkey
            references dogs,
    time       timestamp
);

alter table motion
    owner to apple;

