create table dogs
(
    id       serial not null
        constraint dogs_pkey
            primary key,
    name     varchar,
    resign   timestamp,
    birthday date,
    male     boolean,
    species  varchar
);

alter table dogs
    owner to apple;

