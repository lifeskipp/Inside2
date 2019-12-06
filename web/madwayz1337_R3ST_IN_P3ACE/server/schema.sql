create table users
(
    id         serial       not null
        constraint users_pk
            primary key,
    hash_id varchar(48),
    login varchar(65),
    token varchar(110),
    first_name varchar(65),
    last_name varchar(65),
    algorithm varchar(10) default 'md5'::character varying
);

alter table users
    owner to postgres;

create unique index users_id_uindex
    on users (id);

INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (1, 'c4ca4238a0b923820dcc509a6f75849b', 'root', '<CENSORED> <CENSORED> <CENSORED> <CENSORED> <CENSORED> <CENSORED> <CENSORED> <CENSORED> <CENSORED> <CENSORED>', 'Elon', 'Mask', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (2, 'c81e728d9d4c2f636f067f89cc14862c', 'cTcQjsBp', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Miwicm9sZSI6MH0.Hu4Ey1c3JuuD743-LtZqtSQNg1fSAh7QifZWD4nHDGk', 'Nicholas', 'Harmon', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (3, 'eccbc87e4b5ce2fe28308fd9f2a7baf3', 'aXAhXoUo', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mywicm9sZSI6Mn0.lnFd8smRUu5GAQvZjSf1ZPLiNIL63thGIzCeCEB0ZvM', 'Mark', 'Jones', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (4, 'a87ff679a2f3e71d9181a67b7542122c', 'unJLZDAi', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwicm9sZSI6MX0.D3ql-H_g3mF1J9_BtfXDH0DPA-NH8BiG_ahrvI0X1wU', 'Jennifer', 'Garrett', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (5, 'e4da3b7fbbce2345d7772b0674a318d5', 'qrYCwSvl', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NSwicm9sZSI6MH0.VCF4wP4d9yNdzBIYCSURwKkpF6ngkycmxtZolbChFLY', 'Bailey', 'Hall', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (6, '1679091c5a880faf6fb5e6087eb1b2dc', 'BtMJTZZb', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Niwicm9sZSI6MX0.cOSzarnwWZ1IV6jqbCqPYvHul5zdX8WVO328oGA0DS8', 'Rita', 'Sullivan', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (7, '8f14e45fceea167a5a36dedd4bea2543', 'VpAUvSRM', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Nywicm9sZSI6MH0.aSiXi-JLcCZUlFJbiNfAVPTbu3JV5t_kFQfQvNqRb30', 'Julie', 'Reed', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (8, 'c9f0f895fb98ab9159f51fd0297e236d', 'LYjkInrB', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OCwicm9sZSI6MH0.3WGnr1CYRkKXiKa349nxk2Aoec4m2skfEmz3IvCq5TQ', 'Kevin', 'Roberts', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (9, '45c48cce2e2d7fbdea1afc51c7c6ad26', 'UlTXdOqm', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OSwicm9sZSI6MH0.ZnVLK0uGefp0mSU_9C7CJgVLjx4drKcKgSfQ_Kq9q1Y', 'Dana', 'Russo', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (10, 'd3d9446802a44259755d38e6d163e820', 'KIqVGdUi', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTAsInJvbGUiOjB9.e0diq-bD-Z7erqSJ2RQKz9kzxheuqUVsPZ5yHvITHBA', 'James', 'Gutierrez', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (11, '6512bd43d9caa6e02c990b0a82652dca', 'xFhwVWZZ', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTEsInJvbGUiOjJ9.c8AhMl3LSfFeawaKzYXV2DkhPayBZ2MCSwca-bVqM0A', 'Micheal', 'Baird', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (12, 'c20ad4d76fe97759aa27a0c99bff6710', 'YPFeoMrg', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTIsInJvbGUiOjB9.SAyIR7j74ED4HEX_nXJuYaBKtZk_3UTviI90N101UVg', 'Shawn', 'Gordon', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (13, 'c51ce410c124a10e0db5e4b97fc2af39', 'kwNCZXdf', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTMsInJvbGUiOjF9.jsTIVIZNSK4HvwUOGqlHP0WNLuHmYfg2-loXSFTbWCw', 'Kimberly', 'Ramirez', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (14, 'aab3238922bcc25a6f606eb525ffdc56', 'tDIbGHrQ', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTQsInJvbGUiOjF9._NvEbj65DnvIjZVNnqph0ar7KCB_uyoK8sR-7ThQFuE', 'Christopher', 'Vazquez', 'md5');
INSERT INTO public.users (id, hash_id, login, token, first_name, last_name, algorithm) VALUES (15, '9bf31c7ff062936a96d3c8bd1f8f2ff3', 'KGsfQuRd', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsInJvbGUiOjB9.CuE5Ou-fY_MCwd82_FO4t__kwz8KYsQsTw1sEzNNnWE', 'Steven', 'Villarreal', 'md5');
