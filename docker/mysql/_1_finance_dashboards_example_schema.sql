create table finance_categories
(
    id              int auto_increment
        primary key,
    name            varchar(128) not null,
    parent_category int          null
);

create table finance_institutions
(
    id   int auto_increment
        primary key,
    name varchar(128) not null
)
    comment 'Banks, Credit Cards, etc';

create table finance_accounts
(
    id           int auto_increment
        primary key,
    name         varchar(256) not null,
    institution  int          null,
    balance      double       not null,
    alias        varchar(256) null,
    type         varchar(256) null,
    last_updated datetime     null,
    constraint finance_accounts_finance_institutions_id_fk
        foreign key (institution) references finance_institutions (id)
);

create table finance_vendors
(
    id      int auto_increment
        primary key,
    name    varchar(256) not null,
    aliases varchar(512) null
);

create table finance_transactions
(
    id                   int auto_increment
        primary key,
    date                 datetime     not null,
    description          varchar(256) null,
    original_description varchar(256) null,
    amount               double       null,
    transaction_type     varchar(16)  null,
    category             int          not null,
    merchant             int          not null,
    account              int          not null,
    mail_message_id      varchar(128) not null,
    notes                varchar(256) null,
    constraint finance_transactions_finance_accounts_id_fk
        foreign key (account) references finance_accounts (id),
    constraint finance_transactions_finance_categories_id_fk
        foreign key (category) references finance_categories (id),
    constraint finance_transactions_finance_vendors_id_fk
        foreign key (merchant) references finance_vendors (id)
);

SET PERSIST sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
