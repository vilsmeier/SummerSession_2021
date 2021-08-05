create table account_dog
(
    user_id integer
        constraint account_dog_user_id_fkey
            references account,
    dog_id  integer
        constraint account_dog_dog_id_fkey
            references dogs
);

alter table account_dog
    owner to apple;

