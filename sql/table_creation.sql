CREATE TABLE users (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('TEACHER', 'STUDENT', 'ADMIN')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE courses (
    id UUID PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    teacher_id UUID NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_title_per_teacher UNIQUE (title, teacher_id),
    CONSTRAINT courses_teacher_id_fkey FOREIGN KEY (teacher_id)
        REFERENCES users(id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE lessons
(
    id uuid NOT NULL,
    course_id uuid NOT NULL,
    title character varying(200) NOT NULL,
    content text,
    order_index integer NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT lessons_pkey PRIMARY KEY (id),
    CONSTRAINT lessons_course_id_fkey FOREIGN KEY (course_id)
        REFERENCES public.courses (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)
