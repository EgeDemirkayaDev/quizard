from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Taban


class Test(Taban):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(120), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    short_title = Column(String(120), nullable=True)
    description = Column(Text, nullable=True)
    category = Column(String(80), nullable=True)
    icon = Column(String(20), nullable=True)
    button_text = Column(String(80), nullable=True)
    display_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)

    questions = relationship("Question", back_populates="test", cascade="all, delete-orphan")
    profiles = relationship("ResultProfile", back_populates="test", cascade="all, delete-orphan")


class Question(Taban):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    test_id = Column(Integer, ForeignKey("tests.id", ondelete="CASCADE"), nullable=False)
    text = Column(Text, nullable=False)
    display_order = Column(Integer, default=0)
    is_tiebreaker = Column(Boolean, default=False)
    tiebreaker_order = Column(Integer, nullable=True)

    test = relationship("Test", back_populates="questions")
    options = relationship("Option", back_populates="question", cascade="all, delete-orphan")


class Option(Taban):
    __tablename__ = "options"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    text = Column(Text, nullable=False)
    option_key = Column(String(10), nullable=True)
    display_order = Column(Integer, default=0)

    question = relationship("Question", back_populates="options")
    scores = relationship("OptionScore", back_populates="option", cascade="all, delete-orphan")


class ResultProfile(Taban):
    __tablename__ = "result_profiles"

    id = Column(Integer, primary_key=True, index=True)
    test_id = Column(Integer, ForeignKey("tests.id", ondelete="CASCADE"), nullable=False)
    code = Column(String(80), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    icon = Column(String(20), nullable=True)
    is_hybrid = Column(Boolean, default=False)

    test = relationship("Test", back_populates="profiles")
    scores = relationship("OptionScore", back_populates="profile", cascade="all, delete-orphan")


class OptionScore(Taban):
    __tablename__ = "option_scores"

    id = Column(Integer, primary_key=True, index=True)
    option_id = Column(Integer, ForeignKey("options.id", ondelete="CASCADE"), nullable=False)
    profile_id = Column(Integer, ForeignKey("result_profiles.id", ondelete="CASCADE"), nullable=False)
    score = Column(Float, default=1.0)

    option = relationship("Option", back_populates="scores")
    profile = relationship("ResultProfile", back_populates="scores")


class User(Taban):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    notifications_enabled = Column(Boolean, default=True)
    theme_preference = Column(String(30), default="dark")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Favorite(Taban):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    test_id = Column(Integer, ForeignKey("tests.id", ondelete="CASCADE"), nullable=False)


class SavedTest(Taban):
    __tablename__ = "saved_tests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    test_id = Column(Integer, ForeignKey("tests.id", ondelete="CASCADE"), nullable=False)


class Comment(Taban):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    test_id = Column(Integer, ForeignKey("tests.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class TestResult(Taban):
    __tablename__ = "test_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    test_id = Column(Integer, ForeignKey("tests.id", ondelete="CASCADE"), nullable=False)
    profile_id = Column(Integer, ForeignKey("result_profiles.id", ondelete="SET NULL"), nullable=True)
    result_title = Column(String(255), nullable=False)
    result_description = Column(Text, nullable=False)
    raw_scores = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())