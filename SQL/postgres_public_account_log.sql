create table account_log
(
    user_id     integer     not null
        constraint account_log_user_id_fkey
            references account,
    update_date timestamp   not null,
    password    varchar(60) not null,
    constraint account_log_pkey
        primary key (user_id, update_date)
);

alter table account_log
    owner to apple;

INSERT INTO public.account_log (user_id, update_date, password) VALUES (30020826, '2021-05-12 15:51:12.580189', '$2a$06$DTBjzpgA8VtrQKM2fEoy/OgNb3.Cf7oq2gd5Z9G7i58O79kxUGyhW');
INSERT INTO public.account_log (user_id, update_date, password) VALUES (30020826, '2021-05-12 15:51:21.022867', '$2a$06$fkjLld0ptdsczAAHQYZ2Aem4x.ai3l/q1pOK7RQFvnN2HaipNujuW');
INSERT INTO public.account_log (user_id, update_date, password) VALUES (30020826, '2021-05-12 15:51:24.331645', '$2a$06$FwjAjABDR72aNR/RJpU2h.Z4WYdnbl0mLzJA7C09vTtXeK4g3U59a');
INSERT INTO public.account_log (user_id, update_date, password) VALUES (30020826, '2021-05-12 15:51:27.257852', '$2a$06$ZpvaKFGRyhxtYP65H46tauKBTH1VmjxsGG8elJzWLijGnWXRXMIyy');
INSERT INTO public.account_log (user_id, update_date, password) VALUES (30020826, '2021-05-12 15:51:30.660647', '$2a$06$PuIB4uF0.eeMdTOglpbaHeGNisl2BAMv1B0CWAzgXtr2BeTUeXFn6');
INSERT INTO public.account_log (user_id, update_date, password) VALUES (30020826, '2021-05-12 15:51:32.026844', '$2a$06$rMg5VB6t87WOxk/TSD.p8.o2rVRp1WQ/g4hfUeHa1NDSf3xWS9wiq');
INSERT INTO public.account_log (user_id, update_date, password) VALUES (30020826, '2021-05-12 15:51:33.748209', '$2a$06$Yvs/iu4q3KwzamxRwpFzs.lzmcUoZsjZS3xQ2N/dk0qY7fb0uTc/a');