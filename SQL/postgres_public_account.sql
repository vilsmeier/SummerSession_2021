create table account
(
    id       integer     not null
        constraint account_pkey
            primary key,
    username varchar(20) not null,
    password varchar(60) not null,
    role     varchar(20)
);

alter table account
    owner to apple;

INSERT INTO public.account (id, username, password, role) VALUES (30020826, 'aabbcc', '$2a$06$CPZ0zAENeIZ546N4AgCkdO5nMiZ5YFZwOPwL/g62uqt73TnIHJfbi', 'Teacher');