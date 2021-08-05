create table dog_weight
(
    dog_id integer
        constraint dog_weight_dog_id_fkey
            references dogs,
    weight integer,
    time   timestamp
);

alter table dog_weight
    owner to apple;

